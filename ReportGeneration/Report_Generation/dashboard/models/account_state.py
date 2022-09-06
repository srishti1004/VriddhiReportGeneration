from django.db import models
class Account_State(models.Model):
    account_number=models.CharField(max_length=20,db_column="AccountNumber")
    account_type=models.CharField(max_length=20,db_column="AccountType")
    balance_cb=models.FloatField(db_column="Balance_CB")
    balance_ib=models.FloatField(db_column="Balance_IB")
    balance_ob=models.FloatField(db_column="Balance_OB")
    collstatus_ob= models.CharField(max_length=20,db_column="CollStatus_OB")
    date_of_update=models.DateField(db_column="DateOfUpdate")
    date_ren_ob=models.DateField(db_column="DateRen_OB")
    due=models.FloatField(db_column="Due")
    due_ib=models.FloatField(db_column="Due_IB")
    emi_cb=models.FloatField(db_column="EMI_CB")
    emi_ob=models.FloatField(db_column="EMI_OB")
    emi_due=models.FloatField(db_column="EMIDue")
    emidue_ib=models.FloatField(db_column="EMIDue_IB")
    id=models.BigAutoField(primary_key=True) #check once
    int_due=models.FloatField(db_column="IntDue")
    int_due_ib=models.FloatField(db_column="IntDue_IB")
    int_od_cb=models.FloatField(db_column="IntOD_CB")
    int_od_ob=models.FloatField(db_column="IntOD_OB")
    int_pay_cb=models.FloatField(db_column="IntPay_CB")
    max_due=models.FloatField(db_column="MaxDue")
    max_due_ib=models.FloatField(db_column="MaxDue_IB")
    mem_num=models.CharField(max_length=10,db_column="MemNum")
    Overdue_CB=models.FloatField(db_column="Overdue_CB")
    Overdue_OB=models.FloatField(db_column="Overdue_OB")
    PenalCharge=models.FloatField(db_column="PenalCharge")
    RegBalance_CB=models.FloatField(db_column="RegBalance_CB")
    RegBalance_OB=models.FloatField(db_column="RegBalance_OB")
    RegCharge=models.FloatField(db_column="RegCharge")
    rule=models.TextField(db_column="Rule")
    TotalCharge=models.FloatField(db_column="TotalCharge")
    TotalDue=models.FloatField(db_column="TotalDue")
    TotalDue_IB=models.FloatField(db_column="TotalDue_IB")
    TotalEarn=models.FloatField(db_column="TotalEarn")
    TotalIntDue=models.FloatField(db_column="TotalIntDue")
    TotalIntDue_IB=models.FloatField(db_column="TotalIntDue_IB")
    TotalOD=models.FloatField(db_column="TotalOD")
    TotalOD_IB=models.FloatField(db_column="TotalOD_IB")
    TransferIn_CB=models.FloatField(db_column="TransferIn_CB")
    TransferIn_Tr=models.FloatField(db_column="TransferIn_Tr")
    TransferOut_CB=models.FloatField(db_column="TransferOut_CB")
    TransferOut_Tr=models.FloatField(db_column="TransferOut_Tr")
    type_of_update=models.TextField(db_column="TypeOfUpdate")

    class Meta():
        db_table="newdb_account_state"


