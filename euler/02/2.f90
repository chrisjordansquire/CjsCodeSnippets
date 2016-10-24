program euler2

    implicit none

    Integer ::  n1=1, n2=1, total=0
    Integer :: upper, N, count=0
    Character(len=20) :: arg

    N = iargc()
    if( N<1 ) then
        upper=4e6
    else
        call getarg(1, arg)
        read(arg, *) upper
    endif

    do while( n2 <= upper ) 
        if( mod(n2, 2) == 0) then
            total = total + n2
        endif
        n2 = n1 + n2
        n1 = n2 - n1
    enddo 

    write(*,*) "The sum up to", upper, "is", total

end program euler2
