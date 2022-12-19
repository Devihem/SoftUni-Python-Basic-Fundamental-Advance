size_w = float(input())
size_h = float(input())

if 3 <= size_h <= size_w <= 100:
    cm_size_w = size_w*100
    cm_size_h = size_h*100

    cm_size_h_with_coridor = cm_size_h-100

    max_places_h = cm_size_h_with_coridor//70
    max_places_w = cm_size_w//120

    removing_spaces_for_stuff_fixed = 3

    total_places = max_places_w*max_places_h-removing_spaces_for_stuff_fixed

    print(int(total_places))
