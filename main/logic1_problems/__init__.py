def cigar_party(cigars, is_weekend):
    if 40 < cigars < 60:
        print("cigars are in correct range - always return true")
        return True

    if is_weekend:
        print("its the weekend so doesnt matter how many cigars - always return true")
        return True

    return False


print(cigar_party(20, True))
