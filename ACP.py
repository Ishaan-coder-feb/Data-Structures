bk_nm=["Artemis Fowl","Harry Potter","Magnus Chase","Percy Jackson"," Panchathantra"]
print("The number of books in the list is ",len(bk_nm))
print("The first book is ",bk_nm[0])
print("The last book is ",bk_nm[-1])
print("The rest of the books are ",bk_nm[1:4])
bk_nm.append("Geronimo Stilton")
bk_nm.remove("Magnus Chase")
bk_nm.sort()
print("The new list is ",bk_nm)
bk_nm.reverse()
print("The new list reversed is ",bk_nm)
librarian={"name":"Muneer","age":67,"gender":"male","experience":45}
librarian["experience"]=50
librarian["Email"]="muneer@gmail.com"
librarian.pop("gender")
bk_id=[1,2,3,67,52]
books=dict(zip(bk_nm,bk_id))
print("The final book list is ", books)
print("The final librarian details are ",librarian)

