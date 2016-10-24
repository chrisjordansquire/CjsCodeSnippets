program euler3
    implicit none

    integer, parameter :: sk = selected_int_kind(12)
    integer(kind=sk), parameter :: num=600851475143_sk
    integer(kind=sk), parameter :: upper = sqrt(num*1.0)+1
    integer(kind=sk) :: cur_max=-1, lnum=num
    integer :: i 

    do i=2,upper
        if(mod(lnum, i) == 0) then
            cur_max = i
            do while(mod(lnum, i) == 0)
                lnum = lnum/i
            enddo
        endif
    enddo 

    write(*,*) "The largest prime divisor of ", num, "is", cur_max

end program euler3
