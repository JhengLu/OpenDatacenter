class gNB:
    def __init__(self, gNB_id, connected_rack_id, connected_ue_list):
        self.gNB_id = gNB_id
        self.connected_rack_id = connected_rack_id
        self.connected_ue_list = connected_ue_list

class UE:
    def __init__(self, ue_id, connected_gnb_id):
        self.ue_id = ue_id
        self.connected_gnb_id = connected_gnb_id
