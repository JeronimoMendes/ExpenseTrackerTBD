from uuid import UUID, uuid4

from sqlmodel import delete, select

from app.core.db import Session
from app.models import Expense, ExpenseParticipant, Group, User, Payment
from app.schemas.expenses_schema import ExpenseCreate, PaymentCreate


def create_expense(db: Session, expense: ExpenseCreate, user: User) -> Expense:
    new_expense = Expense(
        id=uuid4(),
        amount=expense.amount,
        description=expense.description,
        date=expense.date,
        created_by=user.id,
        group_id=expense.group_id,
        type=expense.type,
    )
    db.add(new_expense)

    expense_participants = [
        ExpenseParticipant(
            expense_id=new_expense.id,
            user_id=participant.user_id,
            amount=participant.amount,
        )
        for participant in expense.participants
    ]

    for participant in expense_participants:
        db.add(participant)

    return new_expense


def create_payment(db: Session, payment: PaymentCreate, user: User) -> Payment:
    new_payment = Payment(
        id=uuid4(),
        amount=payment.amount,
        date=payment.date,
        created_by=user.id,
        group_id=payment.group_id,
        user_payee_id=payment.user_payee_id,
        user_payer_id=user.id,
    )
    db.add(new_payment)
    return new_payment


def delete_expense(db: Session, expense_id: UUID):
    db.exec(delete(ExpenseParticipant).where(ExpenseParticipant.expense_id == expense_id))
    db.exec(delete(Expense).where(Expense.id == expense_id))


def get_expense(db: Session, expense_id: UUID) -> Expense:
    expense = db.exec(select(Expense).where(Expense.id == expense_id)).first()
    return expense


def get_user_expenses(db: Session, user_id: UUID) -> list[Expense]:
    user = db.exec(select(User).where(User.id == user_id)).first()
    expenses = [participation.expense for participation in user.expenses]
    return expenses


def get_group_expenses(db: Session, group_id: UUID) -> list[Expense]:
    group = db.exec(select(Group).where(Group.id == group_id)).first()
    return group.expenses
