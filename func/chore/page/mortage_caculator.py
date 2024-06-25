import streamlit as st
import pandas as pd
import numpy as np


def calculate_equal_principal(loan_amount, annual_rate, months):
    monthly_rate = annual_rate / 12
    principal_repayment = loan_amount / months
    repayments = []
    for month in range(1, months + 1):
        interest_payment = (loan_amount - principal_repayment * (month - 1)) * monthly_rate
        repayment = principal_repayment + interest_payment
        repayments.append(repayment)
    return repayments


def calculate_equal_payment(loan_amount, annual_rate, months):
    monthly_rate = annual_rate / 12
    repayment = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return [repayment] * months


def mortage_caculator():
    st.title("房贷计算器")
    st.sidebar.header("贷款信息")
    loan = st.sidebar.number_input("贷款额", min_value=0.0, value=0.0)
    rate = st.sidebar.number_input("利率（年利率，%）", min_value=0.0, value=3.95, help="""
    ## 商业贷款
    一年期：3.45|五年期: 3.95
    ## 公积金贷款
    一年期：2.35|五年期: 2.85
    """) / 100
    loan_years = st.sidebar.number_input("贷款年限", min_value=1, value=20)
    loan_months = loan_years * 12
    repayment_method = st.sidebar.selectbox("还款方式", ["等额本金", "等额本息"], help="""
    等额本金：每月还的本金相同，利息根据没还完的本金计算,
    
    等额本息：每月还的金额相同，解方程得到
    """)

    if repayment_method == "等额本金":
        repayments = calculate_equal_principal(loan, rate, loan_months)
    else:
        repayments = calculate_equal_payment(loan, rate, loan_months)

    repayment_schedule = pd.DataFrame({
        "月数": range(1, loan_months + 1),
        "每月还款": repayments,
    })
    repayment_schedule_year = pd.DataFrame({
        "年数": range(1, loan_years+1),
        "每年还款": np.sum(np.reshape(repayments, (-1, 12)), axis=1)
    })
    st.write(f"总贷款额：{loan:.2f} 元")
    st.write(f"总还款额: {sum(repayments):.2f} 元")
    st.write(f"利息: {sum(repayments) - loan:.2f} 元")
    st.write(f"还款/贷款  = {sum(repayments) * 100/ (loan + 0.001):.2f}%")
    st.write(f"贷款年限：{loan_years} 年")
    st.write(f"还款方式：{repayment_method}")

    st.line_chart(repayment_schedule.set_index("月数"))

    c1, c2 = st.columns(2)
    with c1:
        st.dataframe(repayment_schedule, width=500)
    with c2:
        st.dataframe(repayment_schedule_year, width=500)
