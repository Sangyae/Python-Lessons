day1_visitors = {'Bob','Marley','Charlie','Eve'}
day2_visitors = {'Bob','Tamang', 'Mahat','Eve'}

union_result = day1_visitors | day2_visitors
print("Union Using |:", union_result)

union_result_method = day1_visitors.union(day2_visitors)
print("Union using union().", union_result_method)

print("Intersection using &", day1_visitors & day2_visitors)
print("Intersection using intersection()", day1_visitors.intersection(day2_visitors))