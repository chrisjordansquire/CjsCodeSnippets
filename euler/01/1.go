package main

import (
    "fmt"
    "strconv"
)


func main(){
    upper := 1000
    sum := 0
    for i:=0; i<upper; i++{
        if i % 3 == 0 || i % 5 == 0{
            sum += i
        }
    }

    fmt.Println("The sum is " + strconv.Itoa(sum))
}
