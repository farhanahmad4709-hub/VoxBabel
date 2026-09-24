// VoxBabel — WebSocket Client
// Manages connections for audio streaming and caption delivery.

export function createAudioSocket(roomId, onMessage) {
  // TODO: Connect to ws://host/ws/audio/:roomId
}

export function createCaptionSocket(roomId, onCaption) {
  // TODO: Connect to ws://host/ws/captions/:roomId
}

export function createSignalingSocket(roomId, onSignal) {
  // TODO: Connect to ws://host/ws/signaling/:roomId
}
