def viewissuedbook(request):
if request.session.has_key('is_logged'):
       issuedbooks=IssueBook.objects.all()
       lis=[]
       li=[]
       for books in issuedbooks:
           issdate=str(books.issuedate.day)+'-'+str(books.issuedate.month)+'-'+str(books.issuedate.year)
           expdate=str(books.expirydate.day)+'-'+str(books.expirydate.month)+'-'+str(books.expirydate.year)
           print(issdate)
           print(expdate)
           #fine calculation
           days=(date.today()-books.issuedate)
           d=days.days
           fine=0
           if d>15:
               day=d-15
               fine=day*10
           print(d)
           book=list(AddBook.objects.filter(bookid=books.book1))
           students=list(AddStudent.objects.filter(studentid=books.studentid))
           i=0
           for k in book:
               print(li)
               t=(students[i].sname,students[i].studentid,book[i].bookname,book[i].subject,issdate,expdate,fine)
               print(t)
               i=i+1
               lis.append(t)
               print(lis)
       return render(request,'viewissuedbook.html',{'lis':lis})
   return redirect('/')
