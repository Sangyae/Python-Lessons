def binary_search(target, a, left, right):
    l, r = left, right

    while l <= r:
        m = (l + r) // 2
        
        # This returns: 
        #  0 if equal
        # -1 if target is smaller
        #  1 if target is bigger
        comp = (target > a[m]) - (target < a[m])

        if comp == 0:
            return m       # Found it! Return the index
        elif comp < 0:
            r = m - 1      # Target is smaller, ignore right half
        else:
            l = m + 1      # Target is bigger, ignore left half

    return -1              # Not found