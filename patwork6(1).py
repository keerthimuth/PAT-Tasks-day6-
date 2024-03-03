def sort_number(given):
    even_number =[num for num in given if num % 2 == 0]
    odd_number = [num for num in given if num % 2 != 0]
    return even_number,odd_number
    


if __name__=="__main__":
    given = [10,501,22,37,100,999,87,351]
    even_number,odd_number =sort_number(given)
    
    print("The even numbers are:",even_number)
    print("The odd numbers are:",odd_number)
    
    