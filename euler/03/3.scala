import scala.math

var x = BigInt("600851475143")

val upper = math.sqrt(x.toDouble).toInt

var i = 2
var max = 0

while(x != 0 && i<upper){
	
	//println(i + " "+ x)
	if( x%i == 0){
		max = i
		x /= i
		while(x % i ==0){
			x/=i
		}
	}
	i+=1
}

println("The max prime factor is "+max)


