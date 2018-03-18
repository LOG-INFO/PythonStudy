def get_total_page(total_post, num_of_post_of_one_page):
    return (int) ((total_post-1) / num_of_post_of_one_page + 1)


print(get_total_page(0, 10))
print(get_total_page(5, 10))
print(get_total_page(10, 10))
print(get_total_page(13, 10))