ch = (input("Enter: "))

match ch.lower():
    case 'a'|'e'|'i'|'o'|'u' :
        print("Vowel")
    case _ if ch.isalpha():
        print("Consonant ")
    case _ :
        print("Not Valid")