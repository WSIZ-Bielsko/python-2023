from copy import copy

import pytest

from src.job_scheduler.scheduler import Job, Server, can_fit_on_server, schedule_jobs_on_server


@pytest.fixture
def jobs1():
    j1 = Job(1, cpu=4, mem_gb=2.5, priority=10)
    j2 = Job(2, cpu=2, mem_gb=5, priority=50)
    j3 = Job(3, cpu=6, mem_gb=8, priority=100)

    return [j1, j2, j3]


@pytest.fixture
def jobs_large():
    j1 = Job(1, cpu=2, mem_gb=7, priority=10)
    j2 = Job(2, cpu=2, mem_gb=9, priority=50)

    return [j1, j2]


def test_fit(jobs1):
    assert len(jobs1) == 3


def test_two_fixtures(jobs1, jobs_large):
    all_jobs = copy(jobs1)
    all_jobs.extend(jobs_large)
    print(all_jobs)


def test_can_fit(jobs1, jobs_large):
    s = Server(id=1, free_cpu=10, free_mem_gb=7)

    res = [can_fit_on_server(s, j) for j in jobs1]
    assert res == [True, True, False]


def test_schedule1(jobs1):
    s = Server(id=1, free_cpu=12, free_mem_gb=12)
    res = schedule_jobs_on_server(s, jobs1)
    assert res == [jobs1[2], jobs1[0]]
