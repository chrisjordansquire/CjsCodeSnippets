program euler1
    implicit none

    Integer :: N, i, upper, total=0
    Character(len=20) :: arg
    N = IARGC()
if( N < 1) then
    upper = 1000
else
    call getarg(1,arg) 
    read(arg, *) upper
endif

do i=1,upper-1
        if(mod(i,5)==0 .or. mod(i,3)==0) then
            total = total + i
        endif
enddo

write(*,*) "The sum up to", upper, "is", total

end program euler1
