def SignupBackend(request):
    if request.method =='POST':
            uname = request.POST["uname"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email = request.POST["email"]
            phone=request.POST['phone']
            password=request.POST['password']
            userprofile = UserExtend(phone=phone)
            if request.method == 'POST':
                try:
                    UserExists = User.objects.get(username=request.POST['uname'])
                    messages.error(request," Username already taken, Try something else!!!")
                    return redirect("staffsignup")    
                except User.DoesNotExist:
                    if len(uname)>10:
                        messages.error(request," Username must be max 15 characters, Please try again")
                        return redirect("staffsignup")
            
                    if not uname.isalnum():
                        messages.error(request," Username should only contain letters and numbers, Please try again")
                        return redirect("staffsignup")
            
            # create the user
            user = User.objects.create_user(uname, email, password)
            user.first_name=fname
            user.last_name=lname
            user.email = email
            user.save()
            userprofile.user = user
            userprofile.save()
            messages.success(request," Your account has been successfully created")
            return redirect("stafflogin")
    else:
        return HttpResponse('404 - NOT FOUND ')
def LoginBackend(request):
    if request.method =='POST':
        loginuname = request.POST["loginuname"]
        loginpassword=request.POST["loginpassword"]
        RegisteredUser = authenticate(username=loginuname, password=loginpassword)
        if RegisteredUser is not None:
            dj_login(request, RegisteredUser)
            request.session['is_logged'] = True
            RegisteredUser = request.user.id 
            request.session["user_id"] = RegisteredUser
            messages.success(request, " Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request," Invalid Credentials, Please try again")  
            return redirect("/")  
    return HttpResponse('404-not found')
