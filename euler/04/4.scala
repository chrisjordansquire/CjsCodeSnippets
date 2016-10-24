import scala.util.Random

def reverse(x:Int):Int={
	var xcpy = x 
	var y=0
	while(xcpy!=0){
		y *= 10
		y += xcpy%10
		xcpy = (xcpy-(xcpy%10))/10
	}
	return y
}

/*
val gen = new Random()

for(i<-0 until 5){
	val x = gen.nextInt(200)
	println(x + " " + reverse(x))
}
*/

def isPalindrome(x:Int): Boolean={
	return x==reverse(x)
}
	
val upper = 1000
var largest = 0


for(i<-0 until upper){
	for(j<-0 until i+1){
		var prod = i*j		
		//println(prod)
		if(isPalindrome(prod) && prod>largest){
			largest = prod
		}
	}
}

println("The largest product is " + largest)


