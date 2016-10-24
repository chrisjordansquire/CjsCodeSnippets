import java.lang.annotation.Annotation;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;
import java.time.Year;

public class AnnotationAndReflectionExample {

    //Some helpful links:
    // http://stackoverflow.com/questions/20192552/get-value-of-a-parameter-of-an-annotation-in-java
    // http://stackoverflow.com/questions/20362493/how-to-get-annotation-class-name-attribute-values-using-reflection
    // Also, check out the reflections library
    // More recent versions of Guava have a ClassPath object that can be used to look for all classes in
    // a class path


    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface SimpleAnnotation{
        boolean enabled() default true;
    }

    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface AnnotionWithFields{
        String author() default "cjordans";
        // Ideally we could use an actual date object, but very few types of objects can be used
        // as a java annotation field.
        // See: http://stackoverflow.com/questions/1458535/which-types-can-be-used-for-java-annotation-members
        String date();
        int revision() default 1;
        String comments();
    }

    @SimpleAnnotation
    public static int add(int a, int b){
        return a+b;
    }

    @AnnotionWithFields(date="2016-04-15", comments="foo")
    public static int multiply(int a, int b){
        return a*b;
    }

    public static void main(String[] args){
        Annotation[] annotations = AnnotationAndReflectionExample.class.getAnnotations();
        System.out.println(annotations.length); // should be 0

        Method[] methods = AnnotationAndReflectionExample.class.getMethods();
        System.out.println(methods.length);
        try{
            Method addMethod = AnnotationAndReflectionExample.class.getMethod("add", int.class, int.class);
            System.out.println("Found method: " + addMethod.getName());
            System.out.println(" Number of annotations: " + addMethod.getAnnotations().length);
            System.out.println(" Number of declared annotations: " + addMethod.getDeclaredAnnotations().length);
            Annotation addMethodAnnotation = addMethod.getAnnotations()[0];
            System.out.println("  Annotation name: " + addMethodAnnotation.toString());
            SimpleAnnotation simpleAnnotation = addMethod.getAnnotation(SimpleAnnotation.class);
            System.out.println("  Annotation enabled?: " + simpleAnnotation.enabled());

            Method multiplyMethod = AnnotationAndReflectionExample.class.getMethod("multiply", int.class, int.class);
            System.out.println("Found method: " + multiplyMethod.getName());
        }catch(NoSuchMethodException exception){
            System.out.println(exception);
        }


    }
}
