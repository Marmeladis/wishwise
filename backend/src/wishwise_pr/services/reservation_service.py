from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.reservation import Reservation
from wishwise_pr.repositories.reservation_repository import ReservationRepository
from wishwise_pr.services.base_service import BaseService


class ReservationService(BaseService[Reservation]):
    def __init__(self, repository: ReservationRepository):
        super().__init__(repository)
        self.repo: ReservationRepository = repository

    async def reserve(self, gift_id: int, name: str, email: str | None = None) -> Reservation:
        existing = await self.repo.get_by_gift_id(gift_id)
        if existing:
            raise ValueError("Gift already reserved")
        reservation = Reservation(gift_id=gift_id, name=name, email=email)
        return await self.repo.create(reservation)

    async def cancel(self, gift_id: int, email: str | None = None) -> None:
        reservation = await self.repo.get_by_gift_and_email(gift_id, email)
        if reservation:
            await self.repo.delete(reservation.id)
