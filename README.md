# thread-simulation
This program simulates a program with two threads. Each thread runs a different process concurrently.

int y = 3;  x = 0;
void foo () {
	y = y + 1;
	x = y;
}
void bar () {
	y = y * 2;
}
main () {
	Thread t1 = createThread (foo);
	Thread t2 = createThread(bar);
	WaitForAllDone(); 
	cout << x  << y <<endl;
}

