/*
 * iterator_advance.c
 * compile with : -lcstl
 */

#include <stdio.h>
#include <cstl/clist.h>

int main(int argc, char* argv[])
{
    list_t* plist_l1 = create_list(int);
    iterator_t it_l;
    iterator_t it_pos;
    int i = 0;

    if(plist_l1 == NULL)
    {
        return -1;
    }

    list_init(plist_l1);

    for(i = 0; i < 10; ++i)
    {
        list_push_back(plist_l1, i);
    }

    printf("The list is ( ");
    for(it_l = list_begin(plist_l1);
        !iterator_equal(it_l, list_end(plist_l1));
        it_l = iterator_next(it_l))
    {
        printf("%d ", *(int*)iterator_get_pointer(it_l));
    }
    printf(")\n");

    it_pos = list_begin(plist_l1);
    printf("The iterator it_pos initinally points to the first element: %d\n",
        *(int*)iterator_get_pointer(it_pos));

    it_pos = iterator_advance(it_pos, 4);
    printf("The iterator it_pos is advanced 4 steps forward to point to the fifth element: %d\n",
        *(int*)iterator_get_pointer(it_pos));

    it_pos = iterator_advance(it_pos, -3);
    printf("The iterator it_pos is moved 3 steps backward to point to the second element: %d\n",
        *(int*)iterator_get_pointer(it_pos));

    list_destroy(plist_l1);

    return 0;
}
