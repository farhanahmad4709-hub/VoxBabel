// VoxBabel — Zustand Meeting Store
import { create } from 'zustand';

export const useMeetingStore = create((set) => ({
  // ── State ──
  participants: [],
  captions: [],
  myLanguage: 'en',
  isAudioEnabled: true,
  roomId: null,

  // ── Actions ──
  setRoomId: (roomId) => set({ roomId }),

  addParticipant: (participant) =>
    set((state) => ({ participants: [...state.participants, participant] })),

  removeParticipant: (id) =>
    set((state) => ({
      participants: state.participants.filter((p) => p.id !== id),
    })),

  addCaption: (caption) =>
    set((state) => ({ captions: [...state.captions, caption] })),

  clearCaptions: () => set({ captions: [] }),

  setLanguage: (lang) => set({ myLanguage: lang }),

  toggleAudio: () =>
    set((state) => ({ isAudioEnabled: !state.isAudioEnabled })),
}));
