import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_icon="🚦", layout="wide",initial_sidebar_state="expanded")

# Data for 33 Class Classifier
clients_33 = [5, 10, 15]
accuracy_33 = [0.97, 0.955, 0.85]
loss_33 = [0.07, 0.15, 0.35]

# Data for 7 Class Classifier
clients_7 = [5, 10]
accuracy_7 = [0.9833, 0.9781]
loss_7 = [0.0541, 0.0731]

# Sidebar for user input
st.sidebar.title("Select Parameters")
classifier_type = st.sidebar.radio("Choose Classifier Type", ("7 Class Classifier", "33 Class Classifier"))
num_clients = st.sidebar.selectbox("Choose Number of Clients", (5, 10, 15))

# Create a figure for visualization
fig = go.Figure()

# Add data based on user input
if classifier_type == "33 Class Classifier":
    fig.add_trace(go.Scatter(x=clients_33, y=accuracy_33, mode='lines+markers', name='33 Class - Accuracy'))
    fig.add_trace(go.Scatter(x=clients_33, y=loss_33, mode='lines+markers', name='33 Class - Loss'))
else:
    fig.add_trace(go.Scatter(x=clients_7, y=accuracy_7, mode='lines+markers', name='7 Class - Accuracy'))
    fig.add_trace(go.Scatter(x=clients_7, y=loss_7, mode='lines+markers', name='7 Class - Loss'))

# Update layout
fig.update_layout(
    title='Accuracy and Loss for Classifiers',
    xaxis_title='Number of Clients',
    yaxis_title='Value',
    legend_title='Metrics',
    template='plotly_dark'
)

# Display the graph
st.plotly_chart(fig)

# Display the explanation
st.markdown("## Federated Learning Explanation")
st.write("Federated learning is a machine learning technique that enables training models on decentralized data across multiple devices or servers while keeping the data private and secure. Instead of sharing the raw data, the devices collaboratively train a shared model by sending updates to a central server, which aggregates the updates and distributes the updated model back to the devices.")

st.write("### 7 Class Classifier Labels")
st.markdown("""
| Category | Attack Name | Label |
| --- | --- | --- |
| Benign Traffic | Benign Traffic | 0 |
| DDoS and DoS | DDoS-RSTFINFlood | 1 |
|  | DDoS-PSHACK_Flood | 2 |
|  | DDoS-SYN_Flood | 3 |
|  | DDoS-UDP_Flood | 4 |
|  | DDoS-TCP_Flood | 5 |
|  | DDoS-ICMP_Flood | 6 |
""")

st.write("### 33 Class Classifier Labels")
st.markdown("""
| Category | Attack Name | Label |
| --- | --- | --- |
| Benign Traffic | Benign Traffic | 0 |
| DDoS and DoS | DDoS-RSTFINFlood | 1 |
|  | DDoS-PSHACK_Flood | 2 |
|  | DDoS-SYN_Flood | 3 |
|  | DDoS-UDP_Flood | 4 |
|  | DDoS-TCP_Flood | 5 |
|  | DDoS-ICMP_Flood | 6 |
|  | DDoS-SynonymousIP_Flood | 7 |
|  | DDoS-ACK_Fragmentation | 8 |
|  | DDoS-UDP_Fragmentation | 9 |
|  | DDoS-ICMP_Fragmentation | 10 |
|  | DDoS-SlowLoris | 11 |
|  | DDoS-HTTP_Flood | 12 |
|  | DoS-UDP_Flood | 13 |
|  | DoS-SYN_Flood | 14 |
|  | DoS-TCP_Flood | 15 |
|  | DoS-HTTP_Flood | 16 |
| Mirai | Mirai-greeth_flood | 17 |
|  | Mirai-greip_flood | 18 |
|  | Mirai-udpplain | 19 |
| Reconnaissance | Recon-PingSweep | 20 |
|  | Recon-OSScan | 21 |
|  | Recon-PortScan | 22 |
|  | VulnerabilityScan | 23 |
|  | Recon-HostDiscovery | 24 |
| Spoofing | DNS_Spoofing | 25 |
|  | MITM-ArpSpoofing | 26 |
|  | Web BrowserHijacking | 27 |
|  | Backdoor_Malware | 28 |
|  | XSS | 29 |
|  | Uploading_Attack | 30 |
|  | SqlInjection | 31 |
|  | CommandInjection | 32 |
| Other | DictionaryBruteForce | 33 |
""")