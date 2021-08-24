"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each
command will be of the  types listed above. Iterate through each command in order and perform
the corresponding operation on your list."""

if __name__ == '__main__':
    N = int(input())
    arr = []

    for i in range(N):
        number = input().split()
        if number[0] == 'print':
            print(arr)
        elif number[0] == 'insert':
            arr.insert(int(number[1]), int(number[2]))
        elif number[0] == 'remove':
            arr.remove(int(number[1]))
        elif number[0] == 'pop':   
            arr.pop()
        elif number[0] == 'append':
            arr.append(int(number[1]))

        elif number[0] == 'sort':
            arr.sort()
        else:
            arr.reverse()
