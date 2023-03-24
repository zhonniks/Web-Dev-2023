def cigar_party(cigars, is_weekend):
    if is_weekend == False and 40 <= cigars <= 60 : 
        return True
    elif is_weekend and 40 <= cigars : 
        return True
    else:
      return False