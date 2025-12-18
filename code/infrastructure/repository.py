from abc import ABC, abstractmethod


class ExamAttemptRepository(ABC):

    @abstractmethod
    def save(self, attempt):
        pass

    @abstractmethod
    def get_by_id(self, attempt_id):
        pass
