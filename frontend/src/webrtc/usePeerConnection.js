// VoxBabel — WebRTC Peer Connection Hook
// Uses useRef (not useState) for RTCPeerConnection — it's mutable and non-serializable.

export function usePeerConnection() {
  // TODO: Manage RTCPeerConnection lifecycle
  // - Create peer connection with ICE servers
  // - Handle ontrack (remote streams)
  // - Handle onicecandidate (send to signaling server)
  // - Cleanup on unmount
}
