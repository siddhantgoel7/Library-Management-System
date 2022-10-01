def index(request):
    return render(request,'index.html')
def staff(request):
    return render(request,'staff.html')
def stafflogin(request):
    if request.session.has_key('is_logged'):
        return redirect('dashboard')
    return render(request,'stafflogin.html')
def staffsignup(request):
    return render(request,'staffsignup.html')
def dashboard(request):
    if request.session.has_key('is_logged'):
        Book = AddBook.objects.all()
        return render(request,'dashboard.html',{'Book':Book})
    return redirect('stafflogin')
