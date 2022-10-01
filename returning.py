def returnbook(request):
    return render(request,'returnbook.html')
def returnbooksubmission(request):
    if request.method=='POST':
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            bookid2=request.POST['bookid2']
            store1=AddBook.objects.filter(bookid=bookid2)
            def return_book(returnbook):
                if returnbook.category=="Issued":
                    returnbook.category="Not-Issued"
                    obj1=ReturnBook(user=user1,bookid2=bookid2)
                    obj=IssueBook.objects.filter(book1=bookid2)
                    obj.delete()
                    obj1.save()
                    returnbook.save()
                else:
                    messages.error(request," Book not  issued !!!")
            returncategorylist=list(set(map(return_book,store1)))
            Return= ReturnBook.objects.all()
            return render(request,'returnbook.html',{'Return':Return})
    return redirect('/')
