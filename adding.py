def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'addbook.html',{'Book':Book})
def AddBookSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            bookid = request.POST["bookid"]
            bookname = request.POST["bookname"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            add = AddBook(user = user1,bookid=bookid,bookname=bookname,subject=subject,category=category)
            add.save()
            Book = AddBook.objects.all()
            return render(request,'dashboard.html',{'Book':Book})
    return redirect('/')
