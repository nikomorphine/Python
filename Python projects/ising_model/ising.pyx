cimport cython
import numpy as np
from libc.math cimport exp
from libc.stdlib cimport rand
cdef extern from "limits.h":
    int RAND_MAX

def random_spin_field(N, M):
    return np.random.choice([-1, 1], size=(N, M))

import pygame
import pygame.gfxdraw
import sys
import copy

cdef int width = 500
cdef int height = 500
cdef float h = .1
cdef float beta = .4

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

@cython.boundscheck(False)
@cython.wraparound(False)
def draw_field(long [:, :] field):
    cdef int N = field.shape[0]
    cdef int M = field.shape[1]
    cdef int i, j
    for i in range(N):
        for j in range(M):
            if field[i, j] == 1:
                pygame.gfxdraw.pixel(screen, i, j, (255, 255, 255))
            else:
                pygame.gfxdraw.pixel(screen, i, j, (0, 0, 0))

@cython.boundscheck(False)
@cython.wraparound(False)
def cy_ising_step(long [:, :] field, beta = .4, float h = .1):
    cdef int N = field.shape[0]
    cdef int M = field.shape[1]
    cdef int n_offset, m_offset, n, m
    for n_offset in range(2):
        for m_offset in range(2):
            for n in range(n_offset, N, 2):
                for m in range(m_offset, M, 2):
                     _cy_ising_update(field, n, m, beta, h)
    return np.array(field)

cdef _cy_ising_update(long [:, :] field, int n, int m, float beta, float h):
    cdef int total = 0
    cdef int N = field.shape[0]
    cdef int M = field.shape[1]
    if n > 0:
        total += field[n - 1, m]
    if n < N - 1:
        total += field[n + 1, m]
    if m > 0:
        total += field[n, m - 1]
    if m < M - 1:
        total += field[n, m + 1]
    if n > 0 and m > 0:
        total += field[n - 1, m - 1]
    if n < N - 1 and m < M - 1:
        total += field[n + 1, m + 1]
    if m > 0 and n < N - 1:
        total += field[n + 1, m - 1]
    if m < M - 1 and n > 0:
        total += field[n - 1, m + 1]
    cdef float dE = 2 * field[n, m] * total + h * field[n, m]
    if dE <= 0:
        field[n, m] *= -1
    elif exp(-dE * beta) * RAND_MAX > rand():
        field[n, m] *= -1

@cython.boundscheck(False)
@cython.wraparound(False)
def display_ising(long[:, :] field, float beta, float h):
    while True:
        screen.fill((255, 255, 255))

        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        draw_field(field)

        if pygame.key.get_pressed()[pygame.K_UP]:
            h += .1

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            h -= .1

        if pygame.key.get_pressed()[pygame.K_MINUS]:
            beta -= .025

        if pygame.key.get_pressed()[pygame.K_EQUALS]:
            beta += .025

        if pygame.key.get_pressed()[pygame.K_0]:
            beta = 0.1

        if pygame.key.get_pressed()[pygame.K_5]:
            beta = 5

        field = cy_ising_step(field, beta, h)

        pygame.display.set_caption('h=%.2f, beta=%.2f, s_avg=%.2f' % (h, beta, np.average(field)))

        pygame.display.flip()

def _display_ising():
    cdef float h = .1
    cdef float beta = .4
    cdef long[:, :] field = random_spin_field(height, width)
    display_ising(field, beta, h)
    