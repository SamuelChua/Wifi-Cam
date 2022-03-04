import stream
import time

print ("Creating stream class")
tb = stream.stream()

print ("Starting stream...")
tb.start()
print ("Started...")

#Testing the trigger

print ("Saving...")
tb.set_trigger(1)
time.sleep(2)
tb.set_trigger(-1)
print("Stopping...")

time.sleep(2)

print ("Saving...")
tb.set_trigger(1)
time.sleep(2)
tb.set_trigger(-1)
print("Stopping...")