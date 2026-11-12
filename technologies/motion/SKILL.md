# Technology: Motion (formerly Framer Motion)

## 1. Layout Animations and Spring Physics
```tsx
import { motion, AnimatePresence } from "framer-motion";

export function ExpandableCard({ isOpen }: { isOpen: boolean }) {
  return (
    <motion.div
      layout
      transition={{ type: "spring", stiffness: 350, damping: 25 }}
      className="card"
    >
      <motion.h2 layout="position">Interactive Title</motion.h2>
      <AnimatePresence>
        {isOpen && (
          <motion.p
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3 }}
          >
            Detailed content smoothly revealed.
          </motion.p>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
```
