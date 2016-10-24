#include <jni.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

off_t getFileSizeInBytes(const char* fileName){
    struct stat fileInfo;
    lstat(fileName, &fileInfo);
    return fileInfo.st_size;
}

// On Mac, JNICALL is the empty string, and
// JNIEXPORT is __attribute__((visibility("default))
// This attribute merely says that the symbol for Java_ReadFile_loadFile
// should be visible externally. (This attribute is typically used to
// make a symbol not appear to aid with dynamic linking load times.
// See more in Ulrich Drepper's "How To Write Shared Libraries"
// article.)
//
// Also, the jfoo types are, mostly, typedef's
// for the foo type. That's defined in jni.h.
// However, a jstring is a jobject, and a jobject is a pointer
// to a _jobject. Which is left undefined, so jobject's are
// simply pointers.

JNIEXPORT jbyteArray JNICALL Java_ReadFile_loadFile
  (JNIEnv * env, jobject jobj, jstring name){
	  void*  m;
	  jbyteArray jb;
	  jboolean iscopy;
      // Converts the java string name to a pointer to char
      // The lifetime of the pointer to char is managed in the native code
	  const char *mfile = (*env)->GetStringUTFChars(env, name, &iscopy);
      off_t fileSizeInBytes = getFileSizeInBytes(mfile);
	  int fd = open(mfile, O_RDONLY);

	  if(fd == -1){
		  printf("Could not open %s\n", mfile);
	  }
	  m = mmap((caddr_t) 0, fileSizeInBytes, PROT_READ, MAP_PRIVATE, fd, 0);
	  if(m == (caddr_t)-1){
		  printf("Could not mmap %s\n", mfile);
		  return(0);
	  }

	  jb = (*env)->NewByteArray(env, fileSizeInBytes);
	  (*env)->SetByteArrayRegion(env, jb, 0, fileSizeInBytes, (jbyte *)m);
	  close(fd);
      // Tell the JVM the native code is done using the string
	  (*env)->ReleaseStringUTFChars(env, name, mfile);
	  return (jb);
}
