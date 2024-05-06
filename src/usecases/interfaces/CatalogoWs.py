from abc import ABC, abstractmethod
from uuid import UUID
from src.entities.Produto import Produto


class CatalogoWs(ABC):
    @staticmethod
    @abstractmethod
    def obter_produto_por_id(id:  UUID | str) -> Produto:
        pass
