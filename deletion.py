def deletebook(request,id):
    if request.session.has_key('is_logged'):
        AddBook_info = AddBook.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("login")
