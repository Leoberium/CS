#include <iostream>


struct vector {
    size_t arr_size;
    int *left, *right;

    explicit vector(size_t n) {
        this->arr_size = 2 * n;
        this->left = new int[this->arr_size];
        this->right = this->left + n;
        for (int *p = this->left; p != this->right; *(p++) = 0);
    }

    vector(size_t n, int val) {
        this->arr_size = 2 * n;
        this->left = new int[this->arr_size];
        this->right = this->left + n;
        for (int *p = this->left; p != this->right; *(p++) = val);
    }

    void resize() {
        int *arr = new int[2 * this->arr_size];
        for (size_t i = 0; i < this->arr_size; i++) {
            arr[i] = this->left[i];
        }
        delete[] this->left;
        this->left = arr;
        this->right = arr + this->arr_size;
        this->arr_size *= 2;
    }

    void push_back(int val) {
        if (this->right - this->left == this->arr_size) {
            resize();
        }
        *(this->right) = val;
        this->right += 1;
    }

    int pop_back() {
        return *(--this->right);
    }

    int get(size_t pos) const {
        return this->left[pos];
    }

    size_t size() const {
        return this->right - this->left;
    }
};


int vector_test() {
    vector *v;
    v = new vector(2, 10);
    v->push_back(0);
    std::cout << "size " << v->size() << '\n'; // 3
    std::cout << "2 element " << v->get(2) << '\n'; // 0
    std::cout << "1 element " << v->get(1) << '\n'; // 10
    v->push_back(-25);
    v->push_back(35);
    std::cout << "3 element " << v->get(3) << '\n'; // -25
    std::cout << "4 element " << v->get(4) << '\n'; // 35
    v->pop_back();
    v->pop_back();
    std::cout << "size " << v->size() << '\n'; // 3
    v->push_back(5);
    v->push_back(17);
    v->push_back(3);
    std::cout << "0 element " << v->get(0) << '\n'; // 10
    std::cout << "1 element " << v->get(1) << '\n'; // 10
    std::cout << "3 element " << v->get(3) << '\n'; // 5
    std::cout << "size " << v->size() << '\n'; // 6
    return 0;
}

