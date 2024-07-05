package main

type Run struct {
	Time int // in milliseconds
	Results string
	Failed bool
}

//Get average runtime of successful runs in seconds
func averageRuntimeInSeconds(runs []Run) float64 {
