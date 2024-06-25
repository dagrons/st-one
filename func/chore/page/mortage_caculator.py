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
    commercial_loan = st.sidebar.number_input("商业贷款额", min_value=0.0, value=0.0)
    fund_loan = st.sidebar.number_input("公积金贷款额", min_value=0.0, value=0.0)
    commercial_rate = st.sidebar.number_input("商业贷款利率（年利率，%）", min_value=0.0, value=3.95) / 100
    fund_rate = st.sidebar.number_input("公积金贷款利率（年利率，%）", min_value=0.0, value=2.85) / 100
    years = st.sidebar.number_input("贷款年限", min_value=1, value=20)
    months = years * 12

    repayment_method = st.sidebar.selectbox("还款方式", ["等额本金", "等额本息"], help="""
    等额本金：每月还的本金相同，利息根据没还完的本金计算,
    
    等额本息：每月还的金额相同，解方程得到
    """)

    if repayment_method == "等额本金":
        commercial_repayments = calculate_equal_principal(commercial_loan, commercial_rate, months)
        fund_repayments = calculate_equal_principal(fund_loan, fund_rate, months)
    else:
        commercial_repayments = calculate_equal_payment(commercial_loan, commercial_rate, months)
        fund_repayments = calculate_equal_payment(fund_loan, fund_rate, months)

    total_repayments = np.array(commercial_repayments) + np.array(fund_repayments)
    repayment_schedule = pd.DataFrame({
        "月数": range(1, months + 1),
        "每月还款": total_repayments,
    })
    repayment_schedule_year = pd.DataFrame({
        "年数": range(1, months // 12 + 1),
        "每年还款": np.sum(np.reshape(total_repayments, (-1, 12)), axis=1)
    })
    total_loan = commercial_loan + fund_loan
    total_repayments = sum(fund_repayments + commercial_repayments)
    st.write(f"总贷款额：{total_loan:.2f} 元")
    st.write(f"总还款额: {total_repayments:.2f} 元")
    st.write(f"利息: {total_repayments - total_loan:.2f} 元")
    st.write(f"还款/贷款  = {total_repayments * 100/ (commercial_loan + fund_loan + 0.001):.2f}%")
    st.write(f"贷款年限：{years} 年")
    st.write(f"还款方式：{repayment_method}")

    st.line_chart(repayment_schedule.set_index("月数"))

    c1, c2 = st.columns(2)
    with c1:
        st.dataframe(repayment_schedule, width=500)
    with c2:
        st.dataframe(repayment_schedule_year, width=500)
