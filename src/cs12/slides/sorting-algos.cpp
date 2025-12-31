// sorting-algos.cpp - All sorting algorithms in one file
// CS12 - Uncomment one function call at a time to test

#include <iostream>
using namespace std;

// ============== HELPER FUNCTIONS ==============

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// ============== SORTING ALGORITHMS ==============

// O(n^2) - Compare adjacent, swap if wrong order
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1])     // BREAKPOINT: watch arr[j] vs arr[j+1]
                swap(arr[j], arr[j + 1]);
        }
    }
}

// O(n^2) - Find minimum, swap to front
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])   // BREAKPOINT: watch min_idx update
                min_idx = j;
        }
        swap(arr[i], arr[min_idx]);      // BREAKPOINT: watch swap to front
    }
}

// O(n^2) - Insert each element into sorted portion
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];                // BREAKPOINT: watch key value
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];         // BREAKPOINT: watch shift right
            j--;
        }
        arr[j + 1] = key;
    }
}

// Merge helper for mergeSort
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];  // BREAKPOINT: watch merge comparison
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

// O(n log n) - Divide, sort halves, merge
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;  // BREAKPOINT: watch divide
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Partition helper for quickSort (Lomuto scheme)
int partition(int arr[], int low, int high) {
    int pivot = arr[high];               // BREAKPOINT: watch pivot choice
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);        // BREAKPOINT: watch partition swap
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// O(n log n) avg - Pick pivot, partition, recurse
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);  // BREAKPOINT: watch partition index
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// ============== MAIN ==============

int main() {
    int arr[] = {5, 3, 1, 4, 2};
    int n = 5;

    cout << "Original: ";
    printArray(arr, n);

    // Uncomment ONE function call to test:

     bubbleSort(arr, n);
    // selectionSort(arr, n);
    // insertionSort(arr, n);
    // mergeSort(arr, 0, n - 1);
    // quickSort(arr, 0, n - 1);

    cout << "Sorted:   ";
    printArray(arr, n);

    return 0;
}
