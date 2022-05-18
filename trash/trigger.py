import tagged_file_sink_test
import time
import PyQt5

def runApp():
	newApp = PyQt5.QtWidgets.QApplication(sys.argv)
	print ("Creating tagged_file_sink_test class")
	tb = tagged_file_sink_test.tagged_file_sink_test()

	print ("Starting tagged_file_sink_test...")
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

runApp()