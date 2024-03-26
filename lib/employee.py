ef find_by_name(cls, name):

    def reviews(self):
        """Return list of reviews associated with current employee"""
        pass
        from review import Review
        sql = """
            SELECT * FROM reviews
            WHERE employee_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Review.instance_from_db(row) for row in rows
        ]