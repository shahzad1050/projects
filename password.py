import streamlit as st 
import re
st.title("STRONG PASSWORD")
st.header("🔑##make your password stronger##🔐")

password = st.text_input("enter your password",type = "password")

feedback = []
score = 0

if password:
    if len(password) >= 8: 
     score += 1
    else:
       feedback.append("❌passwrod at least 8️⃣ characters")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
       score += 1
    else:
       feedback.append("❌add upper and lowercase")

    if re.search(r"[0-9]",password):
       score += 1
    else:
       feedback.append("❌at least add one digit")

    if re.search(r"[!,@,#,$]" ,password):
     score += 1
    else:
       feedback.append("❌add one spceial characters(!,@,#,$) ")
    if score == 4: 
     feedback.append("✅your password is stronger")
    elif score == 3:
       feedback.append("🟡your password is meduim make is more strong")
    else : 
        feedback.append("🔴your password is weak")

    if feedback:
       st.markdown("improvement suggestions ")
       for tip in feedback:
         st.write(tip)

else:
    st.info("enter your password to start")