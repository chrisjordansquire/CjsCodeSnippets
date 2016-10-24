
object Compute{
	def main(args: Array[String]){
		var x=0
		for(i<-0 to 1000-1){
			if(i%3==0 || i%5==0){
				x+=i
			}
		}
		println(x)
	}
}
