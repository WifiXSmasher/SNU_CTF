from django.shortcuts import render
from .models import CTFs
from .models import UserCTFProgress
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum



# shows all ctf categories on /ctfs page
def ctf_list(request):
    ctftypes = CTFs.CTF_TYPE  # gets all predefined ctf types from model
    return render(request, 'ctfs/ctfs.html', {'ctftypes': ctftypes})  # sends it to template

# shows all ctfs of a specific type
def ctf_type(request, type):
    type_upper = type.upper()  # converts url type to uppercase for matching
    ctf_type_dict = dict(CTFs.CTF_TYPE)  # makes a dict from model choices

    if type_upper not in ctf_type_dict:
        raise Http404("CTF category not found")  # if type is invalid, return 404

    ctfs = CTFs.objects.filter(type=type_upper)  # gets all ctfs of this type
    return render(request, 'ctfs/ctf_type.html', {
        'ctfs': ctfs,
        'type': ctf_type_dict[type_upper]  # sends human-readable type name
    })

@login_required
def ctf_detail(request, type, title):
    type_upper = type.upper()
    ctf = get_object_or_404(CTFs, type=type_upper, title=title)

    if request.method == 'POST':
        user_answer = request.POST.get('answer', '').strip()
        # Assuming you store the correct solution in ctf.solution field
        if user_answer.lower() == ctf.solution.lower():
            # Check if user already solved it
            already_solved = UserCTFProgress.objects.filter(user=request.user, ctf=ctf).exists()
            if already_solved:
                messages.info(request, "You have already solved this challenge and received points.")
            else:
                # Award points
                UserCTFProgress.objects.create(user=request.user, ctf=ctf, points_awarded=ctf.points)
                messages.success(request, f"Correct answer! You earned {ctf.points} points.")
        else:
            messages.error(request, "Incorrect answer. Try again!")

        return redirect('ctf_detail', type=type, title=title)

    return render(request, 'ctfs/ctf_details.html', {'ctf': ctf})

@login_required
def leaderboard(request):
    leaderboard_data = (
        User.objects
        .annotate(total_points=Sum('userctfprogress__points_awarded'))
        .order_by('-total_points')
    )
    return render(request, 'ctfs/leaderboard.html', {'leaderboard': leaderboard_data})
