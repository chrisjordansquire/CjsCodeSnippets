
var x1 = 1
var x2 = 2
var sum = 0

val million = 1000000
val upper = 4*million

while(x2<upper){
	sum += ((x2+1)%2)*x2
	x2 += x1
	x1 = x2-x1
	//println(x1+" "+x2+" "+(x2+1)%2)
}

println(sum)
