#ifndef TASKS_VECTOR_H
#define TASKS_VECTOR_H
// task https://stepik.org/lesson/389706/step/4

struct vector {
    explicit vector(size_t n);
    vector(size_t n, int val);
    void resize();
    void push_back(int val);
    int pop_back();
    int get(size_t pos) const;
    size_t size() const;
};

int vector_test();

#endif
