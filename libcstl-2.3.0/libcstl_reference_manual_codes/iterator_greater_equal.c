/*
 * iterator_greater_equal.c
 * compile with : -lcstl
 */

#include <stdio.h>
#include <cstl/cvector.h>

int main(int argc, char* argv[])
{
    vector_t* pvec_v1 = create_vector(int);
    iterator_t it_vec;
    iterator_t it_pos1;
    iterator_t it_pos2;
    int i = 0;

    if(pvec_v1 == NULL)
    {
        return -1;
    }

    vector_init(pvec_v1);

    for(i = 1; i < 6; ++i)
    {
        vector_push_back(pvec_v1, i * 2);
    }

    printf("The vector v1 is ( ");
    for(it_vec = vector_begin(pvec_v1);
        !iterator_equal(it_vec, vector_end(pvec_v1));
        it_vec = iterator_next(it_vec))
    {
        printf("%d ", *(int*)iterator_get_pointer(it_vec));
    }
    printf(")\n");

    /* Initializing iterator_t it_pos1 and it_pos2 to the first element */
    it_pos1 = iterator_next_n(vector_begin(pvec_v1), 2);
    it_pos2 = iterator_next(vector_begin(pvec_v1));

    printf("The iterator it_pos1 initially points to the third element: %d\n",
        *(int*)iterator_get_pointer(it_pos1));
    printf("The iterator it_pos2 initially points to the second element: %d\n",
        *(int*)iterator_get_pointer(it_pos2));
    if(iterator_greater_equal(it_pos1, it_pos2))
    {
        printf("The iterator it_pos1 is greater than or equal to the iterator it_pos2.\n");
    }
    else
    {
        printf("The iterator it_pos1 is less than the iterator it_pos2.\n");
    }

    it_pos1 = iterator_prev(it_pos1);
    printf("The iterator it_pos1 now points to the second element: %d\n",
        *(int*)iterator_get_pointer(it_pos1));
    if(iterator_greater_equal(it_pos1, it_pos2))
    {
        printf("The iterator it_pos1 is greater than or equal to the iterator it_pos2.\n");
    }
    else
    {
        printf("The iterator it_pos1 is less than the iterator it_pos2.\n");
    }

    it_pos1 = iterator_prev(it_pos1);
    printf("The iterator it_pos1 now points to the first element: %d\n",
        *(int*)iterator_get_pointer(it_pos1));
    if(iterator_greater_equal(it_pos1, it_pos2))
    {
        printf("The iterator it_pos1 is greater than or equal to the iterator it_pos2.\n");
    }
    else
    {
        printf("The iterator it_pos1 is less than the iterator it_pos2.\n");
    }

    vector_destroy(pvec_v1);

    return 0;
}